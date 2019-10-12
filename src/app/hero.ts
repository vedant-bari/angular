export class Hero {
  id: number;
  name: string;
}

// export class User {
//     "email": string;
//     "password": string;
// }
//

// userForm = new FormGroup({
//      email: new FormControl(),
//      password : new FormControl('20')
// });
//
export class User {
    // id: number;
    email: string;
    password1: string;
    password2: string;
    first_name: string;
    last_name: string;
}

export class Token{
  token : string;
}

export class UserToken{
  token: Token;
  user : User;
}

export class Todo
{
            "id": string;
            "created_date": any;
            "modified_date": any;
            "Title":string;
            "text": string;
            "created_by": string;
        }
