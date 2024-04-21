import bpy

bl_info = {
    "name": "Hotkey 'Alt + W' Custom Pie Menu",
    "description": "This is a custom pie menu activated with Alt + W",
    "author": "Fernando Felix",
    "version": (1, 1),
    "blender": (4, 1, 0),
    "location": "3D View -> Alt + W",
    "category": "Custom Pie Menu"
}

# Define a custom operator to set snap_elements_base to {'VERTEX'}
class SetSnapToVertexOperator(bpy.types.Operator):
    """Set Snap to Vertex"""
    bl_idname = "object.set_snap_to_vertex"
    bl_label = "Snap to Vertex"

    def execute(self, context):
        context.scene.tool_settings.snap_elements_base = {'VERTEX'}
        self.report({'INFO'}, "Snap to Vertex enabled")
        return {'FINISHED'}

# Define a custom operator to set snap_elements_base to {'FACE'}
class SetSnapToFaceOperator(bpy.types.Operator):
    """Set Snap to Face"""
    bl_idname = "object.set_snap_to_face"
    bl_label = "Snap to Face"

    def execute(self, context):
        context.scene.tool_settings.snap_elements_base = {'FACE'}
        self.report({'INFO'}, "Snap to Face enabled")
        return {'FINISHED'}
    
# Looptools operators submenu
class LoopToolsMenu(bpy.types.Menu):
    bl_label = "LoopTools"
    bl_idname = "VIEW3D_MT_looptools_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.looptools_flatten", text="Flatten")
        layout.operator("mesh.looptools_relax", text="Relax")
        layout.operator("mesh.looptools_space", text="Space")
        layout.operator("mesh.looptools_circle", text="Circle")
        layout.operator("mesh.looptools_gstretch", text="Gstretch")
        layout.operator("mesh.looptools_bridge", text="Bridge")
        layout.operator("mesh.looptools_spiral", text="Spiral")
        layout.operator("mesh.looptools_curve", text="Curve")
        layout.operator("mesh.looptools_gstretch", text="Gstretch")
        layout.operator("mesh.looptools_flatten", text="Flatten")
        layout.operator("mesh.looptools_relax", text="Relax")
        layout.operator("mesh.looptools_space", text="Space")
        layout.operator("mesh.looptools_circle", text="Circle")
        layout.operator("mesh.looptools_gstretch", text="Gstretch")
        layout.operator("mesh.looptools_bridge", text="Bridge")
        layout.operator("mesh.looptools_spiral", text="Spiral")
        layout.operator("mesh.looptools_curve", text="Curve")
        layout.operator("mesh.looptools_gstretch", text="Gstretch")
        layout.operator("mesh.looptools_flatten", text="Flatten")
        layout.operator("mesh.looptools_relax", text="Relax")
        layout.operator("mesh.looptools_space", text="Space")
        layout.operator("mesh.looptools_circle", text="Circle")
        layout.operator("mesh.looptools_gstretch", text="Gstretch")
        layout.operator("mesh.looptools_bridge", text="Bridge")
        layout.operator("mesh.looptools_spiral", text="Spiral")
        layout.operator("mesh.looptools_curve", text="Curve")
        layout.operator("mesh.looptools_gstretch", text="Gstretch")
        layout.operator("mesh.looptools_flatten", text="Flatten")
        layout.operator("mesh.looptools_relax", text="Relax")
        layout.operator("mesh.looptools_space", text="Space")
        layout.operator("mesh.looptools_circle", text="Circle")
        layout.operator("mesh.looptools_gstretch", text="Gstretch")
        layout.operator("mesh.looptools_bridge", text="Bridge")

# Define an operator to toggle subdivision modifier in edit mode
class ToggleSubdivisionEditModeOperator(bpy.types.Operator):
    """Toggle Subdivision Modifier in Edit Mode"""
    bl_idname = "object.toggle_subdivision_edit_mode"
    bl_label = "Toggle Subdivision in Edit Mode"

    def execute(self, context):
        active_object = context.object
        
        if active_object:
            # Try to access the Subdivision modifier
            modifier = active_object.modifiers.get("Subdivision")
            
            if modifier:
                # Toggle the show_in_editmode property
                modifier.show_in_editmode = not modifier.show_in_editmode
                return {'FINISHED'}
            else:
                self.report({'WARNING'}, "Subdivision modifier not found")
        else:
            self.report({'WARNING'}, "No active object found")
        
        return {'CANCELLED'}

# Define an operator to toggle auto merge vertices
class ToggleAutoMergeOperator(bpy.types.Operator):
    """Toggle the Auto Merge Vertices setting"""
    bl_idname = "object.toggle_auto_merge"
    bl_label = "Auto Merge Vertices"

    def execute(self, context):
        # Toggle the auto merge setting
        context.scene.tool_settings.use_mesh_automerge = not context.scene.tool_settings.use_mesh_automerge
        return {'FINISHED'}

# Define the custom pie menu
class CustomPieMenu(bpy.types.Menu):
    """Custom Pie Menu"""
    bl_label = "Custom Pie Menu"
    bl_idname = "VIEW3D_MT_custom_pie_menu"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # In Object Mode
        if context.mode == 'OBJECT':
            # Add custom snap operators
            pie.operator("object.set_snap_to_vertex", text="Snap to Vertex", icon='VERTEXSEL')
            pie.operator("object.set_snap_to_face", text="Snap to Face", icon='FACESEL')
            
            # Toggle subdivision in edit mode
            pie.operator("object.toggle_subdivision_edit_mode", text="Toggle Subdivision in Edit Mode", icon='MOD_SUBSURF')
            
            # Add a cube
            pie.operator("mesh.primitive_cube_add", text="Add Cube", icon='MESH_CUBE')
            
            # Add an empty
            pie.operator("object.empty_add", text="Add Empty", icon='EMPTY_AXIS').type = 'PLAIN_AXES'
            
            # Add single vertex
            pie.operator("mesh.primitive_vert_add", text="Add Single Vertex", icon='VERTEXSEL')

        # In Edit Mesh Mode
        elif context.mode == 'EDIT_MESH':
            
            # Toggle auto merge vertices
            pie.operator("object.toggle_auto_merge", text="Auto Merge Vertices", icon='MOD_SUBSURF')
            
            # Cursor to selected
            pie.operator("view3d.snap_cursor_to_selected", text="Cursor to Selected", icon='CURSOR')
            
            # Add connect vertices
            pie.operator("mesh.vert_connect_path", text="Connect Vertices", icon='VERTEXSEL')
            
            # Add subdivide operator
            pie.operator("mesh.subdivide", text="Subdivide", icon='MOD_SUBSURF')
            
            # Merge vertices
            pie.operator("mesh.merge", text="Merge at Last", icon='SNAP_VERTEX').type = 'LAST'

            # #Relax mesh
            # pie.operator("mesh.looptools_relax", text="Relax", icon='MOD_SMOOTH')

            # LoopTools submenu
            pie.menu("VIEW3D_MT_looptools_menu")

# Register the operators and menu
def register():
    bpy.utils.register_class(SetSnapToVertexOperator)
    bpy.utils.register_class(SetSnapToFaceOperator)
    bpy.utils.register_class(ToggleSubdivisionEditModeOperator)
    bpy.utils.register_class(ToggleAutoMergeOperator)
    bpy.utils.register_class(CustomPieMenu)
    bpy.utils.register_class(LoopToolsMenu)
    # Register other operators and classes as necessary.

    # Register the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('wm.call_menu_pie', 'W', 'PRESS', alt=True)
    kmi.properties.name = "VIEW3D_MT_custom_pie_menu"

# Unregister the operators and menu
def unregister():
    bpy.utils.unregister_class(SetSnapToVertexOperator)
    bpy.utils.unregister_class(SetSnapToFaceOperator)
    bpy.utils.unregister_class(ToggleSubdivisionEditModeOperator)
    bpy.utils.unregister_class(ToggleAutoMergeOperator)
    bpy.utils.unregister_class(CustomPieMenu)
    bpy.utils.unregister_class(LoopToolsMenu)
    # Unregister other operators and classes as necessary.

    # Unregister the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.get('3D View')
    if km:
        for kmi in km.keymap_items:
            if kmi.properties.name == "VIEW3D_MT_custom_pie_menu":
                km.keymap_items.remove(kmi)

# Ensure the script runs the register function when run directly
if __name__ == "__main__":
    register()
