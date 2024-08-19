const API_URL = 'http://127.0.0.1:5000/api'

const apiService = {
  // Helper function to handle responses
  async handleResponse (response) {
    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.message || 'An error occurred')
    }
    return response.json()
  },

  // GET request
  async get (endpoint) {
    try {
      const response = await fetch(`${API_URL}/${endpoint}`)
      return this.handleResponse(response)
    } catch (error) {
      console.error('API GET Error:', error)
      throw error
    }
  },

  // POST request
  async post (endpoint, data) {
    try {
      const response = await fetch(`${API_URL}/${endpoint}`, {
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
  async put (endpoint, data) {
    try {
      const response = await fetch(`${API_URL}/${endpoint}`, {
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
  async delete (endpoint, data) {
    try {
      const response = await fetch(`${API_URL}/${endpoint}`, {
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

export default apiService
