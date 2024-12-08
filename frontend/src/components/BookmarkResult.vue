<!-- BookmarkResult.vue -->
<template>
    <div class="result-item">
      <h3>{{ result.title }}</h3>
      <span>{{ result.category }}</span>
      <div>
        <button @click="viewDetails">View Details</button>
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
    name: 'BookmarkResult',
    props: {
      result: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        showDetails: false
      }
    },
    methods: {
      viewDetails() {
        this.showDetails = true
      }
    }
}
</script>