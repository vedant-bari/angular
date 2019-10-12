import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { Todo } from '../hero';
import { TodoService} from '../todo.service';
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
  todo : Todo[];
  constructor(private todoService: TodoService) { }

  ngOnInit() {
      this.getTodo();
  }

  getTodo(): void {
    this.todoService.getTodo()
    .subscribe(todo => this.todo = todo);

  }

}
