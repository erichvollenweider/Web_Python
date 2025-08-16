import reflex as rx
import pytz
from datetime import datetime, timedelta


#COMUN
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


image="python-brands-solid-full.svg"


#INDEX
index_title= "Erich Vollenweider | Analista en Computación"
index_description= "Desarrollador de Software"


#PROYECTOS
project_title= "Erich Vollenweider | Proyectos"
project_description= "Proyectos"


#DATE

LOCAL_TIMEZONE_SCRIPT = "Intl.DateTimeFormat().resolvedOptions().timeZone"

WEEKDAYS = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo"
}

MONTHS = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}


def next_date(dates: dict, timezone: str) -> str:

    if len(dates) == 0:
        return ""

    tz = pytz.timezone(timezone)
    now = datetime.now(tz)
    current_time = now.timetz()

    for weekday in range(7):

        current_weekday = str((now.weekday() + weekday) % 7)

        if current_weekday not in dates or dates[current_weekday] == "":
            continue

        print(f"Valor recibido en dates: {dates}")
        hora_limpia = dates[current_weekday].rstrip("h").strip()
        time_utc = datetime.strptime(hora_limpia, "%H:%M").replace(
        tzinfo=pytz.UTC).timetz()

        next_time = datetime.combine(
            now.date(), time_utc).astimezone(tz).timetz()

        if current_time < next_time or weekday > 0:

            next_date = now + timedelta(days=weekday)

            local_date = datetime(
                next_date.year, next_date.month, next_date.day,
                time_utc.hour, time_utc.minute, tzinfo=pytz.UTC).astimezone(tz)

            day = "Hoy" if weekday == 0 else WEEKDAYS[local_date.weekday()]
            zones = timezone.replace('_', ' ').split('/')

            return local_date.strftime(
                f"{day}, %d de {MONTHS[local_date.month]} a las %H:%M | Zona horaria: {zones[len(zones) - 1]}")

    return ""