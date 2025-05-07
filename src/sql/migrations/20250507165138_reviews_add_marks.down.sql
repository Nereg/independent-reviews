BEGIN;

ALTER TABLE IF EXISTS public.reviews
    DROP COLUMN mark;

COMMIT;