export interface ICard {
    professions: IProfession[]
    seens: number
    title: string
    text: string
    team: number
    maxTeam: number
}

export interface IProfession {
    text: string
    color: string
}