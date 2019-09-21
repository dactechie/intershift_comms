<template>
            <editor-menu-bar :editor="editor" v-slot="{ commands, isActive }">
			<div class="menubar">
				<div class="toolbar">
					<button
						class="menubar__button"
						@click="commands.undo"
					>
						<icon name="undo" />
					</button>

					<button
						class="menubar__button"
						@click="commands.redo"
					>
						<icon name="redo" />
					</button>

    <button
          class="menubar__button"
          :class="{ 'is-active': isActive.bold() }"
          @click="commands.bold"
        >
          <icon name="bold" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.italic() }"
          @click="commands.italic"
        >
          <icon name="italic" />
        </button>
<!-- 
        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.strike() }"
          @click="commands.strike"
        > 
          <icon name="strike" />
        </button> -->

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.underline() }"
          @click="commands.underline"
        >
          <icon name="underline" />
        </button>

        <!-- <button
          class="menubar__button"
          :class="{ 'is-active': isActive.code() }"
          @click="commands.code"
        >
          <icon name="code" />
        </button> -->
<!-- 
        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.paragraph() }"
          @click="commands.paragraph"
        >
          <icon name="paragraph" />
        </button> -->

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 1 }) }"
          @click="commands.heading({ level: 1 })"
        >
          H1
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 2 }) }"
          @click="commands.heading({ level: 2 })"
        >
          H2
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 3 }) }"
          @click="commands.heading({ level: 3 })"
        >
          H3
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.bullet_list() }"
          @click="commands.bullet_list"
        >
          <icon name="ul" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.ordered_list() }"
          @click="commands.ordered_list"
        >
          <icon name="ol" />
        </button>

            <button
                class="menubar__button"
                @click="commands.createTable({rowsCount: 3, colsCount: 3, withHeaderRow: false })"
            >
                <icon name="table" />
            </button>

                <span v-if="isActive.table()">
                    <button
                        class="menubar__button"
                        @click="commands.deleteTable"
                    >                        
                        <icon name="remove" />
                    </button>
                    <!-- <button
                        class="menubar__button"
                        @click="commands.addColumnBefore"
                    >
                        <icon name="add_col_before" />
                    </button>
                    <button
                        class="menubar__button"
                        @click="commands.addColumnAfter"
                    >
                        <icon name="add_col_after" />
                    </button>
                    <button
                        class="menubar__button"
                        @click="commands.deleteColumn"
                    >
                        <icon name="delete_col" />
                    </button>
                    <button
                        class="menubar__button"
                        @click="commands.addRowBefore"
                    >
                        <icon name="add_row_before" />
                    </button>
                    <button
                        class="menubar__button"
                        @click="commands.addRowAfter"
                    >
                        <icon name="add_row_after" />
                    </button>
                    <button
                        class="menubar__button"
                        @click="commands.deleteRow"
                    >
                        <icon name="delete_row" />
                    </button>
                    <button
                        class="menubar__button"
                        @click="commands.toggleCellMerge"
                    >
                        <icon name="combine_cells" />
                    </button> -->
                </span>
				</div>
			</div>
		</editor-menu-bar>
</template>
<script>
import Icon from './Icon'
import { EditorMenuBar  } from 'tiptap'

export default {
    components: {
        EditorMenuBar,
	    Icon,
    },
    props:["editor"]
    
}
</script>
<style lang="scss" scoped>
@import "@/assets/sass/variables.scss";
@import '@/assets/sass/menubar.scss';
@import '@/assets/sass/menububble.scss';


</style>