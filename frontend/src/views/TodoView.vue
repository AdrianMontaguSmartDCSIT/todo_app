<template>
    <div class="flex justify-center min-h-screen p-5">
        <div class="flex justify-center w-5/6 sm:w-3/4 md:max-w-lg min-h-[100px] border border-red-500">
            <h1>Todo List</h1>
            <!-- TODO drop down button -->
            <!-- TODO todo list item -->
        </div>

    </div>
</template>

<script>
import { mapStores } from 'pinia'
import { useTodoStore } from '../stores/todoStore';

export default {
    data() {
        return {
            category: "",
            itemToAdd: ""
        }
    },
    computed: {
        // note we are not passing an array, just one store after the other
        // each store will be accessible as its id + 'Store'
        ...mapStores(useTodoStore),
        todoList() {
            return this.todoStore.todoList
        }
    },
    methods: {
        async addCategory() {
            const data = {
                "category": this.category
            }
            try {
                await this.todoStore.createTodoCategory(data)
            } catch (error) {
                alert(error.message)
            }
        },
        async createTodo() {
            const data = {
                "category": this.category,
                "item": this.itemToAdd
            }
            try {
                await this.todoStore.createTodo(data)
                this.itemToAdd = ""
            } catch (error) {
                alert(error)
            }
        },
        async updateTodo() { },
        async deleteTodo() { },
    },
    async mounted() {
        try {
            await this.todoStore.fetchTodoListItems()
            if (Object.keys(this.todoList).length > 0) {
                this.category = Object.keys(this.todoList)[0]
            }
        } catch (error) {
            alert(`${error}`)
        }
    },
}
</script>

<style lang="scss" scoped></style>