from app.application.Interfaces.Iclub_service import IClubService
from app.Domain.Irepos.Iclub_repo import IclubRepository
from app.application.DTOS.club_dto import ClubCreateDTO, ClubUpdateDTO, ClubOutDTO

class ClubService(IClubService):
    def __init__(self, club_repo: IclubRepository):
        self.club_repo = club_repo

    
    def crear_club(self, club_dto: ClubCreateDTO) -> ClubOutDTO:
        # Convertir el DTO a un objeto de dominio
        club = ClubCreateDTO(
            nombre=club_dto.nombre,
            descripcion=club_dto.descripcion,
            fecha_fundacion=club_dto.fecha_fundacion,
            pais=club_dto.pais,
            ciudad=club_dto.ciudad,
            imagen=club_dto.imagen
        )
        club = self.club_repo.crear_club(club)
        return ClubOutDTO.from_orm(club)

    def get_club_by_id(self, club_id: int) -> ClubOutDTO:
        club = self.club_repo.get_club_by_id(club_id)
        return ClubOutDTO.model_validate(club)

    def get_clubes(self) -> list[ClubOutDTO]:
        clubs = self.club_repo.get_clubes()
        return [ClubOutDTO.model_validate(club) for club in clubs]

    def update_club(self, club_dto: ClubUpdateDTO) -> ClubOutDTO:
        club = self.club_repo.actualizar_club(club_dto)
        return ClubOutDTO.model_validate(club)

    def delete_club(self, club_id: int) -> None:
        self.club_repo.eliminar_club(club_id)