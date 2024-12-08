<!-- App.vue -->
<template>
  <div id="app">
    <div class="header">
      <button @click="showBookmarks = !showBookmarks">
        {{ showBookmarks ? 'Lets Search' : 'View Bookmarks' }}
      </button>
    </div>

    <div v-if="!showBookmarks">
      <SearchBar @search-completed="handleSearchResults"/>
      <div class="results-container">
        <SearchResult
          v-for="result in results" 
          :key="result.id" 
          :result="result"
        />
      </div>
    </div>

    <div v-else>
      <div class="results-container">
        <div v-if="bookmarks.length === 0">No bookmarks yet!</div>
        <BookmarkResult
          v-for="result in bookmarks" 
          :key="result.id" 
          :result="result"
        />
      </div>
    </div>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import SearchResult from './components/SearchResult.vue'
import BookmarkResult from './components/BookmarkResult.vue'

export default {
  name: 'App',
  components: {
    SearchBar,
    SearchResult,
    BookmarkResult
  },
  data() {
    return {
      results: [],
      bookmarks: [],
      showBookmarks: false
    }
  },
  methods: {
    handleSearchResults(results) {
      this.results = results
    },
    async fetchBookmarks() {
      try {
        console.log('Fetching bookmarks...')
        const response = await fetch('http://127.0.0.1:5000/bookmarks')
        const data = await response.json()
        console.log('Received data:', data)
        this.bookmarks = data
      } catch (error) {
        console.error('Fetch error:', error)
      }
    }
  },
  mounted() {  
    this.fetchBookmarks()
  },
  watch: {
    showBookmarks(newValue) {
      if (newValue) {
        this.fetchBookmarks()
      }
    }
  }
}
</script>