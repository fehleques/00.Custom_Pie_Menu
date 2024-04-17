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
           
         # Merge Vertex by distance only in mesh edit mode
        if context.mode == 'EDIT_MESH':
            pie.operator("mesh.remove_doubles", text="Merge by Distance", icon='MOD_SUBSURF')


class CustomPieMenu(bpy.types.Menu):
    bl_label = "Custom Pie Menu"
    bl_idname = "VIEW3D_MT_custom_pie_menu"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # Add single vertex in mesh edit mode
        if context.mode == 'EDIT_MESH':
            pie.operator("mesh.primitive_vert_add", text="Add Single Vertex", icon='VERTEXSEL')

        # Subdivide only in mesh edit mode
        if context.mode == 'EDIT_MESH':
            pie.operator("mesh.subdivide", text="Subdivide", icon='MOD_SUBSURF')

        if context.mode == "EDIT_MESH":
            pie.operator("mesh.vert_connect_path", text="Connect Vertices", icon="VERTEXSEL")

        # Merge at last only in mesh edit mode
        if context.mode == 'EDIT_MESH':
            pie.operator("mesh.merge", text="Merge at Last", icon='SNAP_VERTEX').type = 'LAST'

            # Add vertex actions menu only in mesh edit mode
            pie.menu("VIEW3D_MT_vertex_actions", text="Vertex Actions", icon='VERTEXSEL')

    bl_label = "Custom Pie Menu"
    bl_idname = "VIEW3D_MT_custom_pie_menu"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # Add cube operator
        pie.operator("mesh.primitive_cube_add", text="Add Cube", icon='MESH_CUBE')
    
        # Add empty object operator
        if context.mode == 'OBJECT':
            pie.operator("object.empty_add", text="Add Empty", icon='EMPTY_AXIS').type = 'PLAIN_AXES'

        # Add single vertex in mesh edit mode
        if context.mode == 'EDIT_MESH':
            pie.operator("mesh.primitive_vert_add", text="Add Single Vertex", icon='VERTEXSEL')

        # Subdivide only in mesh edit mode
        if context.mode == 'EDIT_MESH':
            pie.operator("mesh.subdivide", text="Subdivide", icon='MOD_SUBSURF')

        # Merge Vertex by distance only in mesh edit mode
        if context.mode == 'EDIT_MESH':
            pie.operator("mesh.remove_doubles", text="Merge by Distance", icon='MOD_SUBSURF')

        # Merge at last only in mesh edit mode
        if context.mode == 'EDIT_MESH':
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
