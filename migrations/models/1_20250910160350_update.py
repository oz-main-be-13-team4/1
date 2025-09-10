from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "user_quote";
        ALTER TABLE "user" ADD "password" VARCHAR(255) NOT NULL;
        ALTER TABLE "user" ADD "gender" VARCHAR(6) NOT NULL  DEFAULT 'other';
        ALTER TABLE "user" ADD "birthday" DATE;
        ALTER TABLE "user" DROP COLUMN "password_hash";
        ALTER TABLE "user" DROP COLUMN "created_at";
        ALTER TABLE "quote" RENAME COLUMN "text" TO "content";
        ALTER TABLE "quote" ALTER COLUMN "author" TYPE VARCHAR(50) USING "author"::VARCHAR(50);
        CREATE TABLE IF NOT EXISTS "user_quote" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "quote_id" INT NOT NULL REFERENCES "quote" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_user_quote_user_id_cf1f0c" UNIQUE ("user_id", "quote_id")
);
COMMENT ON COLUMN "user"."gender" IS 'MALE: male\nFEMALE: female\nOTHER: other';
        CREATE TABLE IF NOT EXISTS "user_question" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "question_id" INT NOT NULL REFERENCES "question" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_user_questi_user_id_2cb8b5" UNIQUE ("user_id", "question_id")
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "password_hash" VARCHAR(200) NOT NULL;
        ALTER TABLE "user" ADD "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "user" DROP COLUMN "password";
        ALTER TABLE "user" DROP COLUMN "gender";
        ALTER TABLE "user" DROP COLUMN "birthday";
        ALTER TABLE "quote" RENAME COLUMN "content" TO "text";
        ALTER TABLE "quote" ALTER COLUMN "author" TYPE VARCHAR(120) USING "author"::VARCHAR(120);
        DROP TABLE IF EXISTS "user_quote";
        DROP TABLE IF EXISTS "user_question";
        CREATE TABLE "user_quote" (
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    "quote_id" INT NOT NULL REFERENCES "quote" ("id") ON DELETE CASCADE
);"""
