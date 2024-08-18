
const API_URL = 'http://localhost:5000/api/todos'

const todoApiService = {
  // Helper function to handle responses
  async handleResponse (response) {
    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.message || 'An error occurred')
    }
    return response.json()
  },

  // GET request
  async get () {
    try {
      const response = await fetch(API_URL)
      return this.handleResponse(response)
    } catch (error) {
      console.error('API GET Error:', error)
      throw error
    }
  },

  // POST request
  async post (data) {
    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
      return this.handleResponse(response)
    } catch (error) {
      console.error('API POST Error:', error)
      throw error
    }
  },

  // PUT request
  async put (data) {
    try {
      const response = await fetch(API_URL, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
      return this.handleResponse(response)
    } catch (error) {
      console.error('API PUT Error:', error)
      throw error
    }
  },

  // DELETE request
  async delete (data) {
    try {
      const response = await fetch(API_URL, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
      return this.handleResponse(response)
    } catch (error) {
      console.error('API DELETE Error:', error)
      throw error
    }
  }
}

export default todoApiService
