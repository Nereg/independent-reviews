BEGIN;

ALTER TABLE IF EXISTS public.subjects
    ADD COLUMN semester smallint NOT NULL;

END;