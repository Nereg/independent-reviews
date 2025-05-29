BEGIN;
-- Reverse the full text search migration
-- Remove in reverse order of creation

-- Drop the search index
DROP INDEX IF EXISTS subjects_search_idx;

-- Drop the search vector column
ALTER TABLE public.subjects DROP COLUMN IF EXISTS search_vector;

-- Drop the immutable unaccent function
DROP FUNCTION IF EXISTS immutable_unaccent(text);

-- Drop the Slovak text search configuration
DROP TEXT SEARCH CONFIGURATION IF EXISTS slovak CASCADE;

-- Drop the Slovak ispell dictionary
DROP TEXT SEARCH DICTIONARY IF EXISTS sk_ispell CASCADE;

-- Drop extensions
DROP EXTENSION IF EXISTS unaccent;
DROP EXTENSION IF EXISTS pg_trgm;

COMMIT;