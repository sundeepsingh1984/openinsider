import configparser
#parser
config_parser=configparser.ConfigParser()

#add_file
config_parser.read("config.ini")


#database section
postgres=config_parser["postgresql"]
POSTGRES_URL=f"postgresql://{postgres['user']}:{postgres['password']}@{postgres['host']}:{postgres['port']}/{postgres['db']}"
POSTGRES_URL_ASYNC = f"postgresql+asyncpg://{postgres['user']}:{postgres['password']}@{postgres['host']}:{postgres['port']}/{postgres['db']}"


