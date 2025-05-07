BEGIN;

ALTER TABLE IF EXISTS public.subjects
    DROP COLUMN semester;

END;