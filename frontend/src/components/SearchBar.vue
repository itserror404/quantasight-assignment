<template>
    <div class="search-container">
      <input 
        v-model="searchTerm" 
        type="text" 
        placeholder="Search..."
      />
      <select v-model="selectedCategory">
        <option value="">All Categories</option>
        <option value="Articles">Articles</option>
        <option value="Reports">Reports</option>
        <option value="Profiles">Profiles</option>
      </select>
      <button @click="search">Search</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SearchBar',
    data() {
      return {
        searchTerm: '',
        selectedCategory: ''
      }
    },
    methods: {
      async search() {
        try {
          const response = await fetch('http://127.0.0.1:5000/search', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              searchTerm: this.searchTerm,
              category: this.selectedCategory
            })
          })
          const results = await response.json()
          this.$emit('search-completed', results)
        } catch (error) {
          console.error('Search error:', error)
        }
      }
    }
  }
  </script>