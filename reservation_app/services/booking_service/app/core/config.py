from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
    mongodb_url:str="mongodb+srv://myAtlasDBUser:Trapdoor619*#!@myatlasclusteredu.ux0czcs.mongodb.net/"
    database_name:str="reservation_app"
    model_config=SettingsConfigDict(env_file=".env",env_file_encoding="utf-8",extra="ignore")
settings=Settings()
