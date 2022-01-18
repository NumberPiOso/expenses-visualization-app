# Expenses

I plan to create a expenses visualization web application for personal use.
This should help me keep track of my incomes and expenses, helping me to take better
decisions.
  
  
I think I will do it using FastAPI and Postgresql at backend, besides that,
may god help me.



**Tasks to do (in priority order)**
- [X] Sample expenses backend api
- [X] Create models and connect it to the database
- [X] Create simple frontend
- [ ] Deploy MVP
    - [X] Docker frontend
    - [X] Docker backend
    - [ ] Docker integration
        - [ ] Mount volumes on docker-compose
        - [ ] Correctly configure url in javascript
    - [ ] Deploy on Azure 
- [ ] Correct database 
- [ ] CI/CD
- [ ] Create users and link them to the movements
- [ ] Create visualizations of expenses using [plotly](https://plotly.com/)


## Development

```Bash
docker-compose up --build
```