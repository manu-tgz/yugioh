
from ..domain.queries import RoundQueries, TournamentQueries

class RoundUseCases:
    
    def create(self, name, tournament_id):
        tournament = TournamentQueries().get(tournament_id)
        
        print(tournament)
        if RoundQueries.is_empty(tournament):
            print("esta vacio")
            self.create_knockout_round(tournament)
        else:
            if RoundQueries.end_round(tournament) is False:
                print("crea otras rondas")  
            else:
                print("se acabo")             
                        
    def create_knockout_round(self,tournament):
        """Create Knockout Round
        Args:
            tournament (Tournament): _description_
        """
        #crear ronda
        round= RoundQueries().create(name="Eliminatoria", tournament=tournament)
        players = TournamentQueries.get_participants(tournament)
        print(players)
        RoundQueries.create_matchs(round,players)
        
                
    

                 
        
        