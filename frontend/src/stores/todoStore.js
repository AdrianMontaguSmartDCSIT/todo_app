import { defineStore } from 'pinia'
import apiService from '../services/api.service'

export const useTodoStore = defineStore('todo', {
  state: () => ({
    todoList: {}
  }),
  actions: {
    async fetchTodoListItems () {
      try {
        this.todoList = await apiService.get('todos')
      } catch (error) {
        throw error
      }
    },
    async createTodo (data) {
      try {
        const response = await apiService.post('todos/item', data)
        this.todoList[data['category']].push(response.item)
        console.log(response.message)
      } catch (error) {
        throw error
      }
    },
    async updateTodo (data) {
      try {
        const response = await apiService.put('todos/item', data)
        const id = response.id
        const name = response.item
        const category = response.category
        this.todoList[category] = this.todoList[category].map(item => {
          if (item.id === id) {
            return { ...item, name: name }
          } else {
            return item
          }
        })

        console.log(response.message)
      } catch (error) {
        throw error
      }
    },
    async deleteTodo (data) {
      try {
        const response = await apiService.delete('todos/item', data)

        this.todoList[data.category] = this.todoList[data.category].filter(
          item => item.id != data.id
        )
        console.log(response.message)
      } catch (error) {
        throw error
      }
    },
    async createTodoCategory (data) {
      try {
        const response = await apiService.delete('todos/category', data)

        this.todoList[response.category] = []

        console.log(response.message)
      } catch (error) {
        throw error
      }
    }
  }
})
