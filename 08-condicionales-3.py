#operadores and y or
# con and se revisa que las dos condiciones se cumplan
usuario_logueado = False
usuario_admin = False
if usuario_logueado and usuario_admin:
    print('Adminsitrador')
elif usuario_logueado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesion')

#puedo ponerle or para que revise que al menos 1 se cumpla de las condiciones
usuario_logueado = True
usuario_admin = False
if usuario_logueado or usuario_admin: #el codigo revisa que al menos 1 se cumpla, entonces se ejecuta la primera que se cumpla
    print('Adminsitrador')
elif usuario_logueado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesion')