<template>
    <div >

        <editor-content :editor="editor"  id="editor"/>
    </div>
</template>
<script>
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
//   History,
} from 'tiptap-extensions'

export default {
  components: {
    EditorContent,
  },
  props: ["value"],
  data() {
    return {
      editor: null,
      editorChange: false
    }
  },
  mounted() {
    this.editor = new Editor({
      onUpdate: ({ getHTML }) => {
        this.editorChange = true;
        this.$emit("input", getHTML());
      },
      content: this.value,
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
        //   new History(),
        ],
    });
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
  }
}
</script>
<style scoped>
#editor {
     border-top: 1px double lightgrey!important; 
     border-left: 1px double lightgrey!important; 
     border-right: 1px double lightgrey!important; 
}
</style>