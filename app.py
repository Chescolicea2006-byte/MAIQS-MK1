import streamlit as st
import time

# Configuración principal de la página
st.set_page_config(
    page_title="Asistente de Diagnóstico Eléctrico", 
    page_icon="⚡", 
    layout="centered"
)

# Encabezado principal
st.title("⚡ Sistema de Diagnóstico Eléctrico con IA")
st.caption("Prototipo de Apoyo a Reparaciones en Piso de Planta — Área de Prueba Eléctrica y Rework")

st.divider()

# Sección de entrada de datos del operador
st.subheader("📋 Registro de Incidencia")

col1, col2 = st.columns(2)

with col1:
    modelo = st.selectbox(
        "Modelo de Vehículo", 
        ["KM74", "MP", "Plataforma General HEV"]
    )
    estacion = st.selectbox(
        "Estación / Área", 
        ["ST-180 (Prueba Eléctrica)", "Línea de Retrabajo (Rework)", "Calidad Final"]
    )

with col2:
    modulo = st.selectbox(
        "Módulo Afectado", 
        ["BCM (Body Control)", "IPDM (Distribución de Potencia)", "ABS / Frenos", "Cluster de Instrumentos"]
    )
    dtc = st.text_input(
        "Código DTC (Opcional)", 
        placeholder="Ej. U0140, B1015, C0035"
    )

sintoma = st.text_area(
    "Descripción del síntoma u observación del operador", 
    placeholder="Ej. Fallo de comunicación CAN en módulo BCM, luces de freno no responden y hay caída de voltaje en conector C2..."
)

# Botón de acción para simular la IA
if st.button("🔍 Generar Diagnóstico con IA", type="primary", use_container_width=True):
    if not sintoma:
        st.warning("⚠️ Por favor ingresa una descripción del problema para consultar la base de datos.")
    else:
        # Simulación visual de tiempo de procesamiento RAG
        with st.spinner("Consultando historial de fallas y manuales de taller..."):
            time.sleep(1.8)
            
            st.success("✅ Diagnóstico generado con éxito a partir del historial de calidad de planta")
            
            # Resultado visual estructurado
            st.markdown("### 🛠️ Solución Recomendada por el Sistema")
            
            # Alerta con la causa raíz
            st.warning("**Causa Raíz Probable (Nivel de Confianza: 94%):** Pérdida de retención mecánica en Pin 4 de conector C2 por sulfatación o desenganche en arnés principal.")
            
            # Procedimiento de reparación
            st.markdown("""
            **Procedimiento estándar de reparación:**
            1. **Seguridad:** Desconectar la batería de 12V y retirar la traba del conector C2 del **módulo BCM**.
            2. **Inspección:** Verificar el asentamiento del **Pin 4**. Si presenta desplazamiento, reinsertar con herramienta de extracción hasta escuchar bloqueo (*click*).
            3. **Prueba:** Aplicar limpiador de contactos dieléctrico y medir continuidad a masa con multímetro.
            4. **Cierre:** Borrar código DTC mediante el escáner y ejecutar ciclo de validación de prueba eléctrica.
            """)
            
            # Información del componente
            st.info("💡 **Pieza/Repuesto de referencia:** Conector C2 (P/N 90123-X) / Arnés Principal BCM")
            
            # Sección de Feedback para mejora continua
            st.divider()
            st.write("**¿Esta solución resolvió la incidencia en la unidad?**")
            
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("👍 Sí, problema resuelto", use_container_width=True):
                    st.balloons()
                    st.success("Registro actualizado. Esta solución incrementó su peso estadístico en el sistema.")
            with col_b:
                if st.button("👎 No, requiero escalar", use_container_width=True):
                    st.error("Reporte enviado a Ingeniería de Calidad para análisis de causa raíz.")
