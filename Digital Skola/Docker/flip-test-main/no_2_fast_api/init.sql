CREATE TABLE pokemon_effect(
   id SERIAL PRIMARY KEY,
   loan_id BIGINT,
   user_id BIGINT,
   pokemon_ability_id INTEGER,
   effect VARCHAR,
   language VARCHAR,
   short_effect VARCHAR
);