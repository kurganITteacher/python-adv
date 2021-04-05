SELECT "mainapp_dialogmemebers"."id",
       "mainapp_dialogmemebers"."dialog_id",
       "mainapp_dialogmemebers"."member_id",
       "mainapp_dialogmemebers"."role",
       "mainapp_dialog"."id",
       "mainapp_dialog"."created",
       "mainapp_dialog"."name",
       "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
  FROM "mainapp_dialogmemebers"
 INNER JOIN "auth_user"
    ON ("mainapp_dialogmemebers"."member_id" = "auth_user"."id")
 INNER JOIN "mainapp_dialog"
    ON ("mainapp_dialogmemebers"."dialog_id" = "mainapp_dialog"."id")
 WHERE "mainapp_dialogmemebers"."member_id" = '2'
 ORDER BY "mainapp_dialog"."created" DESC, "mainapp_dialogmemebers"."role" DESC, "mainapp_dialogmemebers"."member_id" ASC