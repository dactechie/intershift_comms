--exec sp_columns 
--EXEC sp_help tablename
select * from sys.tables

select * from read_messages;
select * from MessageContents;
select * from Messages;

select * from Users;
--select * from MessageStaging;
-- drop table MessageContents;
-- drop table read_messages;
-- drop table Messages;
-- drop table Users;


-- delete from read_messages;
-- delete from MessageContents;
-- delete from Messages;


-- insert into Users (username,color,initials) values ('aftab.jalal','blue','MJ');
-- insert into Users (username,color,initials) values ('meg.diggle','purple','MD');
-- insert into Users (username,color,initials) values ('belinda.grooms','brown','BG');
-- insert into Users (username,color,initials) values ('georgie.catalinac','indigo','GC');
-- insert into Users (username,color,initials) values ('tony.zheng','pink','TZ');
-- insert into Users (username,color,initials) values ('yulya.yulya','teal','YY');
-- insert into Users (username,color,initials) values ('tristan.geier','light-blue','TG');
-- insert into Users (username,color,initials) values ('lei.wang','orange','LW');
-- insert into Users (username,color,initials) values ('melody.nemasango','lime','MN');
-- insert into Users (username,color,initials) values ('shandi.collins','red','SC');
-- insert into Users (username,color,initials) values ('sirpa.kauhanen','amber','SK');

-- insert into Users (public_id,username,_password,color,initials,admin) VALUES
-- ('fc4d703b-3ff5-465f-87ae-0a2b29f5d0d1','aftab.jalal','sha256$7hp3Txtn$0a50398c00f3c5fc639b99ac89564e62c05668804bba2ab24a194c5a04cdf7f3','blue','MJ',1),
-- ('f0503303-dae1-41d6-987a-57b706b73381','meg.diggle','sha256$DmeNzjIR$d56fa674ddbc2df8625c10cdad9e277b2e789d0a10e6ccc4a890d5f52ec00953','purple','MD',1),
-- ('396faace-fe1c-49ea-b248-f1044dcb2631','belinda.grooms','sha256$pVARfKgF$1f03796c35e9dfdaaab4b7d0c5383fe1cc6fb2205065e75674cf6ddcfb6cf420','brown','BG',0),
-- ('a75b3d8c-ca88-4090-9c59-b86ffa4ea88e','georgie.catalinac','sha256$jZkxRn92$9f1e1e4d548b5069218bd422ea1a83f209a367f845620a0194067d61a4e9f8b3','indigo','GC',0),
-- ('826e054b-6be9-4d04-89bb-d2a0e20a6416','tony.zheng','sha256$zq33A2jR$2072f57fc99975ebf6c374b6136c3503a9b6b69e7386b3019c3b3d94971c501d','pink','TZ',0),
-- ('e92964b1-7975-4e28-b153-e2689389024d','yulya.yulya','sha256$8rCa98TS$794c48027f6728fea1e6890385bbfedb9e6fc7a603a893ea5168711f78aa107e','teal','YY',0),
-- ('38a5c614-85f8-4555-9c6d-ec051ce375b0','tristan.geier','sha256$Vad7GUk7$7397bb179396b64b4c4e4dda57ea135c632b11edab8763b2242ab7d44cf0617b','light-blue','TG',0),
-- ('19e97552-a372-4040-8702-97d5942acdeb','lei.wang','sha256$Vl5h5VCl$2de38011d9597b9d2bd00e89e957c59598d6fb4b1248ecb518fda78179d26342','orange','LW',0),
-- ('75df9843-f1fa-4514-869b-0309abcbb069','melody.nemasango','sha256$HJg8doaz$754d8da2ed6a9319abc824315bb2ee717b3e3864b09cea403c35c807f80ad3d3','lime','MN',0),
-- ('5ce44a10-57f9-4f0b-ae94-f90849d0b28e','shandi.collins','sha256$pi0HAVaI$38d920800e94a681cfbdd40121e461d316a7c21797d84a7cae6ca6fabf0ee3a5','red','SC',0),
-- ('feb5da64-ff51-4bdd-95a7-e67ab96db599','sirpa.kauhanen','sha256$ygsVd7E6$2c0e95b4fa61f14d11a8208343ad75019919ea25743a309183f989e16f4f610f','amber','SK',0);