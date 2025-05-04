-- name: registerTelegram :one
WITH tmp_id AS (
	INSERT INTO users (registred)
	VALUES (timezone('utc', now()))
	RETURNING id
)
INSERT INTO public.telegram(
	"telegramId", "userId", "chatId")
	SELECT $1,
    id,
    $2 FROM tmp_id
    RETURNING "userId";
;

-- name: verifyUserByISIC :exec
UPDATE users SET 
    "ISICNum"=sqlc.arg(ISICNum)::bigint,
    "facultyId"=sqlc.arg(facultyId)::int
    WHERE "id"=$1;

-- name: updatePermissions :exec
INSERT INTO permissions ("userId", "permissions") 
VALUES ($1, $2)
ON CONFLICT ("userId") DO UPDATE 
  SET permissions = excluded.permissions;