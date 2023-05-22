from ..domain.queries import ArchetypeQueries

class ArchetypeUseCases():
    def most_popular_in_province(dic):
        return ArchetypeQueries.most_popular_in_province(dic)
    
    def most_popular_in_municipe(dic):
        return ArchetypeQueries.most_popular_in_municipe(dic)