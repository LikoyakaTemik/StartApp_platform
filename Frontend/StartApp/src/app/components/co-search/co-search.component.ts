import { Component, OnInit } from '@angular/core';
import { FormControl } from "@angular/forms";
import { ISearchResult } from 'src/app/models/search-result.model';

@Component({
  selector: 'app-co-search',
  templateUrl: './co-search.component.html',
  styleUrls: ['./co-search.component.scss']
})
export class CoSearchComponent implements OnInit {

  data: string[] = []

  categories: string[] = [
    "Devops",
    "JQuery",
    "Новые",
    "24ч",
    "ML",
    "Data Science",
  ]

  validatedData: ISearchResult[] = []

  searchControl: FormControl;

  constructor() {
    this.searchControl = new FormControl("")
  }

  ngOnInit(): void {
    for (let i = 0; i < 10; i++) {
      this.data.push("Тестовые данные для демонстрации работы поиска Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis hic delectus id, cupiditate natus optio cum. Velit laboriosam perspiciatis nisi labore quis quos aliquam! Hic amet earum, laborum aliquid iste reiciendis totam blanditiis distinctio rem placeat aut vero. Optio iusto, sequi aliquam totam quidem pariatur doloribus fugit natus temporibus incidunt hic magni modi dolorum placeat iure repellendus explicabo! Velit, eaque?")
    }
    this.searchControl.valueChanges.subscribe((search_data) => {

      if (search_data.length == 0){
        document.getElementById("pre-results")?.classList.add("invisible")
      }
      else {
        document.getElementById("pre-results")?.classList.remove("invisible")
        this.validatedData = []
        for (let i=0; i < this.data.length; i++){
          let lowercaseData = this.data[i].toLowerCase()
          let lowercase2Search = search_data.toLowerCase()
          if (lowercaseData.includes(lowercase2Search)){
            this.comparedToHtml(lowercaseData, lowercase2Search)
          }
          if (this.validatedData.length >= 10){
            break
          }
        }
        console.log(this.validatedData)
      }
    })
  }

  comparedToHtml(result: string, query: string) {
    let i = result.indexOf(query)
    let pre = result.slice(0, i).split(" ")
    console.log(pre)
    if (pre.length >= 2){
      pre = [pre[pre.length - 2], pre[pre.length - 1]]
    }
    console.log(pre)
    let post = result.slice(i + query.length).split(" ")
    if (post.length >= 5) {
      post = post.slice(0, 6)
    }
    console.log(post)
    let founded = result.slice(i, i + query.length).split(" ")
    let searchResult: ISearchResult = {
      'pre': pre.join(" "),
      'founded': founded.join(" "),
      'post': post.join(" "),
      'link': ""
    }
    this.validatedData.push(searchResult)
  }
}
