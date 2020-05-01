create table stores
(
	storeID int auto_increment,
	storeName varchar(200) not null,
	address varchar(200) not null,
	telephone varchar(40) null,
	constraint stores_pk
		primary key (storeID)
);

create index stores_storeName_index
	on stores (storeName desc);

commit;