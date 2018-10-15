BEGIN;
--
-- Add field image to post
--
ALTER TABLE "blog_post" RENAME TO "blog_post__old";
CREATE TABLE "blog_post" ("image" varchar(100) NULL, "idpost" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(300) NOT NULL, "content" text NOT NULL, "date" date NOT NULL, "textcontent" text NOT NULL, "author" varchar(50) NOT NULL, "section" varchar(50) NOT NULL);
INSERT INTO "blog_post" ("idpost", "title", "content", "date", "textcontent", "author", "section", "image") SELECT "idpost", "title", "content", "date", "textcontent", "author", "section", NULL FROM "blog_post__old";
DROP TABLE "blog_post__old";
--
-- Add field tags to post
--
ALTER TABLE "blog_post" RENAME TO "blog_post__old";
CREATE TABLE "blog_post" ("idpost" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(300) NOT NULL, "content" text NOT NULL, "date" date NOT NULL, "textcontent" text NOT NULL, "author" varchar(50) NOT NULL, "section" varchar(50) NOT NULL, "image" varchar(100) NULL, "tags" text NOT NULL);
INSERT INTO "blog_post" ("idpost", "title", "content", "date", "textcontent", "author", "section", "image", "tags") SELECT "idpost", "title", "content", "date", "textcontent", "author", "section", "image", 'general' FROM "blog_post__old";
DROP TABLE "blog_post__old";
COMMIT;
