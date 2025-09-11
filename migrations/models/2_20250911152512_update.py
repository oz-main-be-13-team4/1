from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ALTER COLUMN "password" TYPE VARCHAR(50) USING "password"::VARCHAR(50);
        ALTER TABLE "diary" ADD "user_id" INT NOT NULL;
        ALTER TABLE "diary" ADD "weather" VARCHAR(2);
        ALTER TABLE "diary" ADD "mood" VARCHAR(2);
        ALTER TABLE "diary" ADD "update_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "diary" ALTER COLUMN "title" TYPE VARCHAR(100) USING "title"::VARCHAR(100);
        ALTER TABLE "diary" ADD CONSTRAINT "fk_diary_user_9023c106" FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "diary" DROP CONSTRAINT IF EXISTS "fk_diary_user_9023c106";
        ALTER TABLE "user" ALTER COLUMN "password" TYPE VARCHAR(255) USING "password"::VARCHAR(255);
        ALTER TABLE "diary" DROP COLUMN "user_id";
        ALTER TABLE "diary" DROP COLUMN "weather";
        ALTER TABLE "diary" DROP COLUMN "mood";
        ALTER TABLE "diary" DROP COLUMN "update_at";
        ALTER TABLE "diary" ALTER COLUMN "title" TYPE VARCHAR(200) USING "title"::VARCHAR(200);"""
