<!-- SearchResult.vue -->
<template>
    <div class="result-item">
      <h3>{{ result.title }}</h3>
      <span>{{ result.category }}</span>
      <div>
        <button @click="viewDetails">View Details</button>
        <button @click="handleBookmark" :disabled="isBookmarked">
          {{ isBookmarked ? 'Bookmarked!' : 'Bookmark' }}
        </button>
      </div>

      <!-- Details Modal -->
      <div v-if="showDetails">
        <h2>{{ result.title }}</h2>
        <p>{{ result.description }}</p>
        <p>Category: {{ result.category }}</p>
        <p>Author: {{ result.author }}</p>
        <p>Published: {{ result.published_date }}</p>
        <p>URL: {{ result.url }}</p>
        <button @click="showDetails = false">Close</button>
      </div>
    </div>
</template>
  
<script>
export default {
    name: 'SearchResult',
    props: {
      result: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        isBookmarked: false,
        showDetails: false
      }
    },
    methods: {
      viewDetails() {
        this.showDetails = true
      },
      async handleBookmark() {
        try {
          const response = await fetch('http://127.0.0.1:5000/bookmarks', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              result: this.result.id
            })
          })
          if (response.ok) {
            this.isBookmarked = true
          }
        } catch (error) {
          console.error('Bookmark error:', error)
        }
      }
    }
}
</script>