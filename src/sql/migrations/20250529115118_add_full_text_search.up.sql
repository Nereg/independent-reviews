BEGIN;
-- this is a very complex migration, see sql/fulltext_search
-- create extensions needed for full text search
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS unaccent;

-- create search dict
CREATE TEXT SEARCH DICTIONARY sk_ispell (
    TEMPLATE = ispell,
    DictFile = sk_SK,
    AffFile = sk_SK,
    StopWords = czech
);

-- create search config
CREATE TEXT SEARCH CONFIGURATION slovak( COPY = simple );
ALTER TEXT SEARCH CONFIGURATION slovak
    ALTER MAPPING FOR hword, hword_part, word
    WITH sk_ispell;

-- create an immutable wrapper around unaccent
CREATE OR REPLACE FUNCTION immutable_unaccent(text)
RETURNS text 
LANGUAGE sql 
IMMUTABLE 
STRICT 
AS $function$
    SELECT unaccent($1)
$function$;

-- create a search vector
ALTER TABLE PUBLIC.SUBJECTS
ADD COLUMN IF NOT EXISTS SEARCH_VECTOR TSVECTOR GENERATED ALWAYS AS (
	SETWEIGHT(TO_TSVECTOR('slovak',IMMUTABLE_UNACCENT (COALESCE(SUBJECTS."name", ''))),'A') ||
	SETWEIGHT(TO_TSVECTOR('simple',IMMUTABLE_UNACCENT (COALESCE(SUBJECTS."aisCode", ''))),'B')
) STORED;

-- create an index over the search vector

CREATE INDEX subjects_search_idx ON subjects USING GIN (search_vector);

COMMIT;