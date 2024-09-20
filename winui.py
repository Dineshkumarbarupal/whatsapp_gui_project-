# winui.py
from win32more.xaml import XamlApplication
from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Media import MicaBackdrop
from win32more.Microsoft.UI.Xaml.Markup import XamlReader

class App(XamlApplication):
    def OnLaunched(self, args):
        try:
            # Create window object
            win = Window()
            # Apply Mica backdrop effect
            win.SystemBackdrop = MicaBackdrop()

            # Load the XAML content from the file
            with open("page.xaml", "r", encoding='utf-8') as file:
                xaml_content = file.read()
                win.Content = XamlReader.Load(xaml_content)

            # Activate the window once content is loaded
            win.Activate()

        except Exception as e:
            print(f"Error loading XAML or activating window: {e}")

# Start the application
XamlApplication.Start(App)
