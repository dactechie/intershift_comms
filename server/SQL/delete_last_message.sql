
-- begin TRANSACTION
    declare @mid int;
    set @mid = (select top 1 m.id from Messages m order by created_date desc);
    delete from read_messages where message_id = @mid;
    delete from MessageContents where message_id  = @mid;
    delete from Messages  where id = @mid;
-- go;


-- in (
--     select top 1 m.id from Messages m order by created_date desc   
-- );


--- delete all messages 
-- delete from read_messages;
-- delete from MessageContents;
-- delete from Messages;

