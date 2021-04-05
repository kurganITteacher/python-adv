SELECT "mainapp_dialogmemebers"."id",
       "mainapp_dialogmemebers"."dialog_id",
       "mainapp_dialogmemebers"."member_id",
       "mainapp_dialogmemebers"."role",
       "mainapp_dialog"."id",
       "mainapp_dialog"."created",
       "mainapp_dialog"."name"
  FROM "mainapp_dialogmemebers"
 INNER JOIN "mainapp_dialog"
    ON ("mainapp_dialogmemebers"."dialog_id" = "mainapp_dialog"."id")
 WHERE "mainapp_dialogmemebers"."member_id" = '2'
 ORDER BY "mainapp_dialog"."created" DESC, "mainapp_dialogmemebers"."role" DESC, "mainapp_dialogmemebers"."member_id" ASC