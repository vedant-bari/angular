import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { Todo } from '../hero';
import { TodoService } from '../todo.service';
import { AlertService } from '../alert.service';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-todo',
  templateUrl: './todo.component.html',
  styleUrls: ['./todo.component.css']
})
export class TodoComponent implements OnInit {

  todoForm: FormGroup;
  loading = false;
  submitted = false;
  returnUrl: string;
  error: string;
  todo: Todo[];
  next: string;
  previous: string;
  count: string;
  url: string = 'http://127.0.0.1:8000/api/v1/todo/todolistcreate/';
  constructor(private todoService: TodoService) { }

  ngOnInit() {
    this.getTodo(this.url);
  }

  getTodo(url: string): void {
    this.todoService.getTodo2(url)
      .subscribe(todo => {
        console.log(todo)
        this.todo = todo['results'];
        this.next = todo['next'];
        this.previous = todo['previous'];
        this.count = todo['count'];
        console.log()

      });
  }

  onPageChanged(url: string) {
    this.getTodo(url);
  }
}
