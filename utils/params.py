class Params:
    __ReqresOnPageNumber = 0
    __AuthorName = ''
    __tags = []

    def getReqresOnPageNumber(self, pageNumber):
        self.__ReqresOnPageNumber = pageNumber
        return self.__ReqresOnPageNumber

    def getAuthorName(self, authorName):
        self.__AuthorName = authorName
        return self.__AuthorName

    def getTags(self, tags):
        self.__tags = tags
        return self.__tags
