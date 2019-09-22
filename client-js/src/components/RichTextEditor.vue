<template>
    <div class="editor">
        <RichTextMenubar :editor="editor" />
         
        <editor-content class="editor__content" :editor="editor"  />

        <!-- <div class="suggestion-list" v-show="showSuggestions" ref="suggestions"> -->
      <!-- <template v-if="hasResults">
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
    </div>-->



    </div>
</template>
<script>
// import Fuse from 'fuse.js'
// import tippy from 'tippy.js'
import { Editor, EditorContent} from 'tiptap'
import RichTextMenubar from './RichTextMenubar'
import {
//   Blockquote,

  HardBreak,
 Heading,
  OrderedList,
 BulletList,
  ListItem,
  //TodoItem,
  //TodoList,
		Table,
		TableHeader,
		TableCell,
		TableRow,
  Bold,
   Code,
 Italic,
//   Link,
  //Strike,
   Underline,
   History,
} from 'tiptap-extensions'


export default {
  components: {
    EditorContent,
    RichTextMenubar,
  },
  props: ["value"],
  data() {
    return {
      editor: new Editor({
      onUpdate: ({ getHTML }) => {
        this.editorChange = true;
        this.$emit("input", getHTML());
      },
      content: "<br/>",
    //   `<ul data-type="todo_list">
    //         <li data-type="todo_item" data-done="true">
    //           Buy beer
    //         </li> `,
      extensions:  [
            new HardBreak(),
            new Heading(),
            new OrderedList(),
            new BulletList(),
            new ListItem(),
           // new TodoItem(),
           // new TodoList(),

            new Bold(),
            new Code(),
            new Italic(),
          //  new Strike(),
            new Underline(),
            new History(),
 
            new Table({
                resizable: true,
                }),
            new TableHeader(),
            new TableCell(),
            new TableRow(),
          
        ],
    //       query: null,
    //   suggestionRange: null,
    //   filteredUsers: [],
    //   navigatedUserIndex: 0,
    //   insertMention: () => {},
    //   observer: null,
    })
      ,
      editorChange: false
    }
  },
//   mounted() {
//     console.log("Mounted Rich text editor")
//   },
// computed: {
//     hasResults() {
//         if (this.filteredUsers)
//           return this.filteredUsers.length
//         return 0
//     },
//     showSuggestions() {
//       return this.query || this.hasResults
//     },
//   },
  beforeDestroy() {
    if (this.editor) this.editor.destroy();
  },
//   watch: {
//     value(val) {
//       if (this.editor && !this.editorChange) {
//         this.editor.setContent(val, true);
//       }
//       this.editorChange = false;
//     }
//   },
methods: {
    /*
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
    },*/
  }

}
</script>

<style lang="scss" >

@import '@/assets/sass/main.scss';
// //@import "~variables";
// ul[data-type="todo_list"] {
//   padding-left: 0;
// }
// li[data-type="todo_item"] {
//   display: flex;
//   flex-direction: row;
// }
// .todo-checkbox {
//   border: 2px solid $color-black;
//   height: 0.9em;
//   width: 0.9em;
//   box-sizing: border-box;
//   margin-right: 10px;
//   margin-top: 0.3rem;
//   user-select: none;
//   -webkit-user-select: none;
//   cursor: pointer;
//   border-radius: 0.2em;
//   background-color: transparent;
//   transition: 0.4s background;
// }
// .todo-content {
//   flex: 1;
//   > p:last-of-type {
//     margin-bottom: 0;
//   }
//   > ul[data-type="todo_list"] {
//     margin: .5rem 0;
//   }
// }
// li[data-done="true"] {
//   > .todo-content {
//     > p {
//       text-decoration: line-through;
//     }
//   }
//   > .todo-checkbox {
//     background-color: $color-black;
//   }
// }
// li[data-done="false"] {
//   text-decoration: none;
// }
// .editor p.is-empty:first-child::before {
//   content: attr(data-empty-text);
//   float: left;
//   color: #aaa;
//   pointer-events: none;
//   height: 0;
//   font-style: italic;
// }
</style>