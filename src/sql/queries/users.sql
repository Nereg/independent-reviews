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

-- name: getUserByTelegramId :one
SELECT "userId" FROM telegram WHERE "telegramId" = $1;

-- name: verifyUserByIsic :exec
UPDATE users SET 
    "ISICNum"=$1,
    "facultyId"=$2,
    "aisId"=$3
    WHERE "id"=$4;

-- name: getUser :one
SELECT * FROM users WHERE "id"=$1;

-- name: updatePermissions :exec
INSERT INTO permissions ("userId", "permissions") 
VALUES ($1, $2)
ON CONFLICT ("userId") DO UPDATE 
  SET permissions = excluded.permissions;