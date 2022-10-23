import { Component, OnInit } from '@angular/core';
import { ICard } from 'src/app/models/card.model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  cards: ICard[] = [{
    seens: 1000,
    maxTeam: 5,
    team: 3,
    title: "Центр правового обеспечения природопользования",
    text: "Разработчик ПО, обеспечивающего автоматизацию документооборота, соблюдение природоохранных законодательных требований, снижение экологических рисков организаций, рисков в области охраны труда и промышленной безопасности.",
    professions: [{text: "frontend", color: "#FAFF00"}, {text: "backend", color: "#FF0000"}, {text: "devops", color: "#00FF29"}, {text: "engineer", color: "#FF00FF"}]
  }]

  constructor() {
    for (let i = 0; i < 10; i++){
      this.cards.push({
        seens: 1000,
        maxTeam: 5,
        team: 3,
        title: "Lorem Ipsum - это текст-\"рыба\", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной \"рыбой\" Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsu...",
        text: "В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus...",
        professions: [{text: "frontend", color: "#FAFF00"}, {text: "backend", color: "#FF0000"}, {text: "devops", color: "#00FF29"}, {text: "engineer", color: "#FF00FF"}]
      })
    }
  }

  ngOnInit(): void {
  }

}
