"""
Sistema de Inscripciones - Escuela Técnica
Problema de Evaluación Final

Autor: Carol Pusey Rose
Fecha: Mayo 2025
Curso: Fundamentos de Programación
"""

import os


class EscuelaTecnica:
    def __init__(self):
        # Definición de cursos según la tabla proporcionada
        self.cursos = {
            1: {
                'nombre': 'Programación',
                'costo_mensual': 300000,
                'duracion': 6,
                'descuento': 0.20  # 20%
            },
            2: {
                'nombre': 'Diseño Gráfico',
                'costo_mensual': 250000,
                'duracion': 4,
                'descuento': 0.15  # 15%
            },
            3: {
                'nombre': 'Redes',
                'costo_mensual': 200000,
                'duracion': 5,
                'descuento': 0.10  # 10%
            }
        }

        # Lista para almacenar estudiantes inscritos
        self.estudiantes = []

    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def formatear_moneda(self, cantidad):
        """Formatea una cantidad como moneda colombiana"""
        return f"${cantidad:,.0f} COP".replace(',', '.')

    def mostrar_titulo(self):
        """Muestra el título del programa"""
        print("=" * 60)
        print("🎓 SISTEMA DE INSCRIPCIONES - ESCUELA TÉCNICA 🎓")
        print("=" * 60)
        print()

    def mostrar_cursos(self):
        """Muestra la información de todos los cursos disponibles"""
        print("📚 CURSOS DISPONIBLES:")
        print("-" * 60)
        print(
            f"{'ID':<3} {'Curso':<15} {'Costo/Mes':<15} {'Duración':<10} {'Descuento'}")
        print("-" * 60)

        for curso_id, info in self.cursos.items():
            print(f"{curso_id:<3} {info['nombre']:<15} "
                  f"{self.formatear_moneda(info['costo_mensual']):<15} "
                  f"{info['duracion']} meses{'':<3} {int(info['descuento']*100)}%")
        print()

    def mostrar_modalidades_pago(self):
        """Muestra las modalidades de pago disponibles"""
        print("💳 MODALIDADES DE PAGO:")
        print("-" * 40)
        print("1. Pago Completo (con descuento)")
        print("2. Pago Mensual (sin descuento)")
        print()

    def validar_entrada_numerica(self, mensaje, min_val, max_val):
        """Valida entrada numérica dentro de un rango"""
        while True:
            try:
                valor = int(input(mensaje))
                if min_val <= valor <= max_val:
                    return valor
                else:
                    print(
                        f"❌ Error: Ingrese un número entre {min_val} y {max_val}")
            except ValueError:
                print("❌ Error: Ingrese un número válido")

    def inscribir_estudiante(self):
        """Inscribe un nuevo estudiante"""
        print("✏️ INSCRIBIR NUEVO ESTUDIANTE")
        print("-" * 40)

        # Solicitar nombre del estudiante
        while True:
            nombre = input("Nombre del estudiante: ").strip()
            if nombre:
                break
            print("❌ Error: El nombre no puede estar vacío")

        # Mostrar cursos disponibles
        self.mostrar_cursos()

        # Seleccionar curso
        curso_id = self.validar_entrada_numerica(
            "Seleccione el curso (1-3): ", 1, 3
        )

        # Mostrar modalidades de pago
        self.mostrar_modalidades_pago()

        # Seleccionar modalidad de pago
        modalidad = self.validar_entrada_numerica(
            "Seleccione modalidad de pago (1-2): ", 1, 2
        )

        # Obtener información del curso
        curso_info = self.cursos[curso_id]
        costo_total = curso_info['costo_mensual'] * curso_info['duracion']

        # Calcular descuento y costo final
        descuento_aplicado = 0
        costo_final = costo_total

        if modalidad == 1:  # Pago completo
            descuento_aplicado = costo_total * curso_info['descuento']
            costo_final = costo_total - descuento_aplicado
            tipo_pago = "Pago Completo"
        else:  # Pago mensual
            tipo_pago = "Pago Mensual"

        # Crear registro del estudiante
        estudiante = {
            'nombre': nombre,
            'curso_id': curso_id,
            'curso_nombre': curso_info['nombre'],
            'duracion': curso_info['duracion'],
            'costo_total': costo_total,
            'descuento_aplicado': descuento_aplicado,
            'costo_final': costo_final,
            'tipo_pago': tipo_pago
        }

        # Agregar a la lista de estudiantes
        self.estudiantes.append(estudiante)

        # Mostrar confirmación
        print("\n✅ INSCRIPCIÓN EXITOSA")
        print("-" * 30)
        print(f"Estudiante: {nombre}")
        print(f"Curso: {curso_info['nombre']}")
        print(f"Modalidad: {tipo_pago}")
        print(f"Costo total: {self.formatear_moneda(costo_total)}")
        if descuento_aplicado > 0:
            print(f"Descuento: -{self.formatear_moneda(descuento_aplicado)}")
        print(f"Valor a pagar: {self.formatear_moneda(costo_final)}")

        input("\nPresione Enter para continuar...")

    def mostrar_estudiantes_inscritos(self):
        """Muestra la lista de estudiantes inscritos"""
        if not self.estudiantes:
            print("📝 No hay estudiantes inscritos")
            return

        print(f"👥 ESTUDIANTES INSCRITOS ({len(self.estudiantes)} total)")
        print("-" * 80)
        print(
            f"{'#':<3} {'Nombre':<20} {'Curso':<15} {'Modalidad':<15} {'Valor Final'}")
        print("-" * 80)

        for i, estudiante in enumerate(self.estudiantes, 1):
            print(f"{i:<3} {estudiante['nombre']:<20} "
                  f"{estudiante['curso_nombre']:<15} "
                  f"{estudiante['tipo_pago']:<15} "
                  f"{self.formatear_moneda(estudiante['costo_final'])}")
        print()

    def generar_reporte_final(self):
        """Genera y muestra el reporte final con todos los resultados"""
        if not self.estudiantes:
            print("❌ No hay estudiantes inscritos para generar reporte")
            input("Presione Enter para continuar...")
            return

        print("📊 REPORTE FINAL")
        print("=" * 60)

        # 1. Cantidad de estudiantes por curso
        estudiantes_por_curso = {}
        for curso_id, info in self.cursos.items():
            estudiantes_por_curso[info['nombre']] = 0

        # 2. Duración total en meses
        duracion_total = 0

        # 3. Costo total sin descuentos
        costo_total_sin_descuento = 0

        # 4. Monto total de descuentos
        total_descuentos = 0

        # 5. Valor neto final
        valor_neto_final = 0

        # Procesar cada estudiante
        for estudiante in self.estudiantes:
            estudiantes_por_curso[estudiante['curso_nombre']] += 1
            duracion_total += estudiante['duracion']
            costo_total_sin_descuento += estudiante['costo_total']
            total_descuentos += estudiante['descuento_aplicado']
            valor_neto_final += estudiante['costo_final']

        # Mostrar resultados
        print("1. CANTIDAD DE ESTUDIANTES POR CURSO:")
        print("-" * 40)
        for curso, cantidad in estudiantes_por_curso.items():
            if cantidad > 0:
                print(
                    f"   • {curso}: {cantidad} estudiante{'s' if cantidad > 1 else ''}")

        print(f"\n2. DURACIÓN TOTAL DE TODOS LOS CURSOS:")
        print("-" * 40)
        print(f"   {duracion_total} meses")

        print(f"\n3. COSTO TOTAL SIN DESCUENTOS:")
        print("-" * 40)
        print(f"   {self.formatear_moneda(costo_total_sin_descuento)}")

        print(f"\n4. MONTO TOTAL DE DESCUENTOS APLICADOS:")
        print("-" * 40)
        print(f"   -{self.formatear_moneda(total_descuentos)}")

        print(f"\n5. VALOR NETO FINAL (DESPUÉS DE DESCUENTOS):")
        print("-" * 40)
        print(f"   {self.formatear_moneda(valor_neto_final)}")

        print("\n" + "=" * 60)
        input("Presione Enter para continuar...")

    def mostrar_menu(self):
        """Muestra el menú principal"""
        print("🔹 MENÚ PRINCIPAL")
        print("-" * 30)
        print("1. Ver cursos disponibles")
        print("2. Inscribir estudiante")
        print("3. Ver estudiantes inscritos")
        print("4. Generar reporte final")
        print("5. Salir")
        print()

    def ejecutar(self):
        """Método principal que ejecuta el programa"""
        while True:
            self.limpiar_pantalla()
            self.mostrar_titulo()
            self.mostrar_menu()

            opcion = self.validar_entrada_numerica(
                "Seleccione una opción (1-5): ", 1, 5)

            if opcion == 1:
                self.limpiar_pantalla()
                self.mostrar_titulo()
                self.mostrar_cursos()
                self.mostrar_modalidades_pago()
                input("Presione Enter para continuar...")

            elif opcion == 2:
                self.limpiar_pantalla()
                self.mostrar_titulo()
                self.inscribir_estudiante()

            elif opcion == 3:
                self.limpiar_pantalla()
                self.mostrar_titulo()
                self.mostrar_estudiantes_inscritos()
                input("Presione Enter para continuar...")

            elif opcion == 4:
                self.limpiar_pantalla()
                self.mostrar_titulo()
                self.generar_reporte_final()

            elif opcion == 5:
                self.limpiar_pantalla()
                print("👋 ¡Gracias por usar el Sistema de Inscripciones!")
                print("🎓 Escuela Técnica - Hasta pronto")
                break


def main():
    """Función principal del programa"""
    try:
        escuela = EscuelaTecnica()
        escuela.ejecutar()
    except KeyboardInterrupt:
        print("\n\n👋 Programa terminado por el usuario")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor, contacte al administrador del sistema")


if __name__ == "__main__":
    main()
