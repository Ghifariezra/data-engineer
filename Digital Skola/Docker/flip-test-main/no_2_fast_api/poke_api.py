from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import asyncpg

app = FastAPI()
DATABASE_URL = "postgresql://poke:p0k3!!123@postgres/pokebase"

class EffectRequest(BaseModel):
    loan_id: str
    user_id: str
    pokemon_ability_id: str

async def get_pool():
    return await asyncpg.create_pool(DATABASE_URL)

@app.post("/pokemon_effect/")
async def pokemon_effect(effect_request: EffectRequest):
    loan_id = effect_request.loan_id
    user_id = effect_request.user_id
    pokemon_ability_id = effect_request.pokemon_ability_id

    try :
        url = "https://pokeapi.co/api/v2/ability/" + pokemon_ability_id
        call = requests.get(url)
        response = call.json()
        
        pool = await get_pool()
        returned_entries = []
        async with pool.acquire() as conn:
            for effect_entries in response['effect_entries'] :
                await conn.execute("""
                    INSERT INTO pokemon_effect (loan_id, user_id, pokemon_ability_id, effect, language, short_effect)
                    VALUES ($1, $2, $3, $4, $5, $6);
                """, int(loan_id), int(user_id), int(pokemon_ability_id), str(effect_entries['effect']), 
                str(effect_entries['language']), str(effect_entries['short_effect']))
                returned_entries.append(effect_entries)

        return {
            "loan_id": loan_id,
            "user_id": user_id,
            "pokemon_ability_id": pokemon_ability_id,
            "returned_entries" : returned_entries
        }

    except (Exception) as e :
        return {
            "error" : str(e)
        }