import bpy

bl_info = {
    "name": "Hotkey 'Alt + W' Custom Pie Menu",
    "description": "This is a custom pie menu activated with Alt + W",
    "author": "Fernando Felix",
    "version": (1, 0),
    "blender": (4, 1, 0),
    "location": "3D View -> Alt + W",
    "category": "Custom Pie Menu"
}

class VertexActions(bpy.types.Menu):
    bl_label = "Vertex Actions"
    bl_idname = "VIEW3D_MT_vertex_actions"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # Add single vertex
        pie.operator("mesh.primitive_circle_add", text="Add Single Vertex", icon='VERTEXSEL').vertices = 1

        # Toggle subdivision surface modifier in edit mode
        # Use an operator to toggle the subdivision modifier visibility in edit mode.
        pie.operator("object.modifier_toggle_viewport", text="Toggle Subdivision Surface", icon='MOD_SUBSURF').modifier = "Subdivision"

# Define the Custom Pie Menu class
class CustomPieMenu(bpy.types.Menu):
    bl_label = "Custom Pie Menu"
    bl_idname = "VIEW3D_MT_custom_pie_menu"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # Add cube operator
        pie.operator("mesh.primitive_cube_add", text="Add Cube", icon='MESH_CUBE')
    
        # Add empty object operator
        pie.operator("object.empty_add", text="Add Empty", icon='EMPTY_AXIS').type = 'PLAIN_AXES'

        # Check if we are in mesh edit mode before showing the merge operator
        if context.active_object and context.active_object.mode == 'EDIT' and context.active_object.type == 'MESH':
            pie.operator("mesh.merge", text="Merge at Last", icon='SNAP_VERTEX').type = 'LAST'

            # Add vertex actions menu only in mesh edit mode
            pie.menu("VIEW3D_MT_vertex_actions", text="Vertex Actions", icon='VERTEXSEL')

# Register function
def register():
    bpy.utils.register_class(CustomPieMenu)
    bpy.utils.register_class(VertexActions)

    # Register the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('wm.call_menu_pie', 'W', 'PRESS', alt=True)
    kmi.properties.name = "VIEW3D_MT_custom_pie_menu"

# Unregister function
def unregister():
    bpy.utils.unregister_class(CustomPieMenu)
    bpy.utils.unregister_class(VertexActions)

    # Unregister the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.get('3D View')
    if km:
        for kmi in km.keymap_items:
            if kmi.properties.name == "VIEW3D_MT_custom_pie_menu":
                km.keymap_items.remove(kmi)

if __name__ == "__main__":
    register()
