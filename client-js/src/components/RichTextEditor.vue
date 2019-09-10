<template>
    <div >

        <editor-content :editor="editor"  id="editor"/>

        <div class="suggestion-list" v-show="showSuggestions" ref="suggestions">
      <template v-if="hasResults">
        <div
          v-for="(user, index) in filteredUsers"
          :key="user.id"
          class="suggestion-list__item"
          :class="{ 'is-selected': navigatedUserIndex === index }"
          @click="selectUser(user)"
        >
          {{ user.name }}
        </div>
      </template>
      <div v-else class="suggestion-list__item is-empty">
        No users found
      </div>
    </div>


    </div>
</template>
<script>
import Fuse from 'fuse.js'
import tippy from 'tippy.js'
import { Editor, EditorContent } from 'tiptap'
import {
//   Blockquote,
//   CodeBlock,
//   HardBreak,
//  Heading,
//   OrderedList,
//  BulletList,
//   ListItem,
//   TodoItem,
//   TodoList,
  Bold,
//   Code,
//  Italic,
//   Link,
//   Strike,
  Underline,
   History,
   Mention,
} from 'tiptap-extensions'

export default {
  components: {
    EditorContent,
  },
  props: ["value"],
  data() {
    return {
      editor: new Editor({
      onUpdate: ({ getHTML }) => {
        this.editorChange = true;
        this.$emit("input", getHTML());
      },
      content: " <br/>     ",
      extensions:  [
        //   new Blockquote(),
        //   new CodeBlock(),
        //   new HardBreak(),
        //   new Heading({ levels: [1, 2, 3] }),
        //   new BulletList(),
        //   new OrderedList(),
        //   new ListItem(),
        //   new TodoItem(),
        //   new TodoList(),
          new Bold(),
        //   new Code(),
        //   new Italic(),
        //   new Link(),
        //   new Strike(),
          new Underline(),
          new History(),
          new Mention({
            // a list of all suggested items
            items: () => [
              { id: 1, name: 'Jason' },
              { id: 2, name: 'Taylor' },
              { id: 6, name: 'Dora ' },
            ],
            // is called when a suggestion starts
            onEnter: ({
              items, query, range, command, virtualNode,
            }) => {
              this.query = query
              this.filteredUsers = items
              this.suggestionRange = range
              this.renderPopup(virtualNode)
              // we save the command for inserting a selected mention
              // this allows us to call it inside of our custom popup
              // via keyboard navigation and on click
              this.insertMention = command
            },
            // is called when a suggestion has changed
            onChange: ({
              items, query, range, virtualNode,
            }) => {
              this.query = query
              this.filteredUsers = items
              this.suggestionRange = range
              this.navigatedUserIndex = 0
              this.renderPopup(virtualNode)
            },
            // is called when a suggestion is cancelled
            onExit: () => {
              // reset all saved values
              this.query = null
              this.filteredUsers = []
              this.suggestionRange = null
              this.navigatedUserIndex = 0
              this.destroyPopup()
            },
            // is called on every keyDown event while a suggestion is active
            onKeyDown: ({ event }) => {
              // pressing up arrow
              if (event.keyCode === 38) {
                this.upHandler()
                return true
              }
              // pressing down arrow
              if (event.keyCode === 40) {
                this.downHandler()
                return true
              }
              // pressing enter
              if (event.keyCode === 13) {
                this.enterHandler()
                return true
              }
              return false
            },
            // is called when a suggestion has changed
            // this function is optional because there is basic filtering built-in
            // you can overwrite it if you prefer your own filtering
            // in this example we use fuse.js with support for fuzzy search
            onFilter: (items, query) => {
              if (!query) {
                return items
              }
              const fuse = new Fuse(items, {
                threshold: 0.2,
                keys: ['name'],
              })
              return fuse.search(query)
            },
          }),
        ],
          query: null,
      suggestionRange: null,
      filteredUsers: [],
      navigatedUserIndex: 0,
      insertMention: () => {},
      observer: null,
    })
      ,
      editorChange: false
    }
  },
  mounted() {
    
  },
computed: {
    hasResults() {
        if (this.filteredUsers)
          return this.filteredUsers.length
        return 0
    },
    showSuggestions() {
      return this.query || this.hasResults
    },
  },
  beforeDestroy() {
    if (this.editor) this.editor.destroy();
  },
  watch: {
    value(val) {
      if (this.editor && !this.editorChange) {
        this.editor.setContent(val, true);
      }
      this.editorChange = false;
    }
  },
methods: {
    // navigate to the previous item
    // if it's the first item, navigate to the last one
    upHandler() {
      this.navigatedUserIndex = ((this.navigatedUserIndex + this.filteredUsers.length) - 1) % this.filteredUsers.length
    },
    // navigate to the next item
    // if it's the last item, navigate to the first one
    downHandler() {
      this.navigatedUserIndex = (this.navigatedUserIndex + 1) % this.filteredUsers.length
    },
    enterHandler() {
      const user = this.filteredUsers[this.navigatedUserIndex]
      if (user) {
        this.selectUser(user)
      }
    },
    // we have to replace our suggestion text with a mention
    // so it's important to pass also the position of your suggestion text
    selectUser(user) {
      this.insertMention({
        range: this.suggestionRange,
        attrs: {
          id: user.id,
          label: user.name,
        },
      })
      this.editor.focus()
    },
    // renders a popup with suggestions
    // tiptap provides a virtualNode object for using popper.js (or tippy.js) for popups
    renderPopup(node) {
      if (this.popup) {
        return
      }
      this.popup = tippy(node, {
        content: this.$refs.suggestions,
        trigger: 'mouseenter',
        interactive: true,
        theme: 'dark',
        placement: 'top-start',
        inertia: true,
        duration: [400, 200],
        showOnInit: true,
        arrow: true,
        arrowType: 'round',
      })
      // we have to update tippy whenever the DOM is updated
      if (MutationObserver) {
        this.observer = new MutationObserver(() => {
          this.popup.popperInstance.scheduleUpdate()
        })
        this.observer.observe(this.$refs.suggestions, {
          childList: true,
          subtree: true,
          characterData: true,
        })
      }
    },
    destroyPopup() {
      if (this.popup) {
        this.popup.destroy()
        this.popup = null
      }
      if (this.observer) {
        this.observer.disconnect()
      }
    },
  }

}
</script>

<style lang="css">

.mention {
  background: rgba(black, 0.1);
  color: rgba(black, 0.6);
  font-size: 0.8rem;
  font-weight: bold;
  border-radius: 5px;
  padding: 0.2rem 0.5rem;
  white-space: nowrap;
}
.mention-suggestion {
  color: rgba(black, 0.6);
}
.suggestion-list {
  padding: 0.2rem;
  border: 2px solid rgba(black, 0.1);
  font-size: 0.8rem;
  font-weight: bold;
  /* __no-results {
    padding: 0.2rem 0.5rem;
  } */
}
 .suggestion__item {
    border-radius: 5px;
    padding: 0.2rem 0.5rem;
    margin-bottom: 0.2rem;
    cursor: pointer;
 }
 .suggestion__item:last-child {
      margin-bottom: 0;
    }
 .suggestion__item.is-selected,
 .suggestion__item:hover {
      background-color: rgba(white, 0.2);
    }
 .suggestion__item.is-empty {
      opacity: 0.5;
    }
.tippy-tooltip.dark-theme {
  background-color: black;
  padding: 0;
  font-size: 1rem;
  text-align: inherit;
  color: white;
  border-radius: 5px;
}
.tippy-tooltip.tippy-backdrop {
    display: none;
  }
.tippy-tooltip.tippy-roundarrow {
    fill: black;
  }
.tippy-tooltip.tippy-popper[x-placement^=top],
.tippy-tooltip.tippy-arrow {
    border-top-color: black;
  }
.tippy-tooltip.tippy-popper[x-placement^=bottom],
.tippy-tooltip.tippy-arrow {
    border-bottom-color: black;
}
  .tippy-tooltip.tippy-popper[x-placement^=left],
  .tippy-tooltip.tippy-arrow {
    border-left-color: black;
  }
  .tippy-tooltip.tippy-popper[x-placement^=right],
  .tippy-tooltip.tippy-arrow {
    border-right-color: black;
}
</style>
