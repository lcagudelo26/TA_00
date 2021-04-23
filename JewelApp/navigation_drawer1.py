#navigation_helper para menu de opiniones
navigation_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Opiniones'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:5
                        md_bg_color: 189/255,189/255,189/255,1
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            background_color: 0,150/255,136/255,1
            ContentNavigationDrawer:
            
                orientation: 'vertical'
                
                padding: "8dp"
                spacing: "8dp"
                MDLabel:
                    text: "Opiniones"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                    color: 1,1,1,1
                    bg_color: 0,150/255,136/255,1
                    canvas.before:
                        Color:
                            rgba: 0,150/255,136/255,1
                        Rectangle:
                            size: self.size
                            pos: self.pos
                MDLabel:
                    text: "Categorias"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                    color: 1,1,1,1
                    canvas.before:
                        Color:
                            rgba: 0,150/255,136/255,1
                        Rectangle:
                            size: self.size
                            pos: self.pos
           
                ScrollView:
                    DrawerList:
        
                           
                        id: md_list
                     
                        MDList:
                            OneLineIconListItem:
                                text: "Lo más comentado"
                                bg_color: 1,193/255,7/255,1
                            
                                    
                         
                            OneLineIconListItem:
                                text: "Libros"
                                bg_color: 1,193/255,7/255,1
                            
                            
                                    
                           
                            OneLineIconListItem:
                                text: "Peliculas & Series"
                                bg_color: 1,193/255,7/255,1
                                
                            
                            OneLineIconListItem:
                                text: "Restaurantes & Lugares"
                                bg_color: 1,193/255,7/255,1
      
                            OneLineIconListItem:
                                text: "Servicios & Productos"  
                                bg_color: 1,193/255,7/255,1
                                                                                              
                            OneLineIconListItem:
                                divider:
                                text_color: 33/255, 33/255, 33/255, 1
                                bg_color: 1,193/255,7/255,1
                                                                    
                            OneLineIconListItem:
                                text: "Otros" 
                                bg_color: 1,193/255,7/255,1                          
                            OneLineIconListItem:
                                text: "Opina sobre algo nuevo"
                                bg_color: 1,193/255,7/255,1                                
                            
                            
"""