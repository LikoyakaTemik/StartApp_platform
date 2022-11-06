import { Component, Input, OnInit } from '@angular/core';
import { ICard } from 'src/app/models/card.model';

@Component({
  selector: 'app-co-card',
  templateUrl: './co-card.component.html',
  styleUrls: ['./co-card.component.scss']
})
export class CoCardComponent implements OnInit {

  @Input() card!: ICard

  constructor() {}

  ngOnInit(): void {
  }

}
