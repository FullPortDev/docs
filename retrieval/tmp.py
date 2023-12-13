class Collection:
    def __init__(self) -> None:
        self.state = 'unloaded'
    
    async def load(self):
        self.state = 'loading'

        # TODO : async requests call to GET /collections 
        # TODO : add a try catch setting state to error, and saving self.error_message

        self.state = 'loaded'

    async def loading(self):
        # TODO implement if state = 'loaded'
        pass



async def main():
    col = Collection()

    col.load()

    await col.loading


# TODO start the main method