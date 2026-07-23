<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asistente de Diagnóstico Eléctrico - Planta de Ensamble</title>
    <style>
        :root {
            --primary: #004085;
            --secondary: #0056b3;
            --bg: #eef2f5;
            --card: #ffffff;
            --text: #212529;
            --success: #28a745;
            --warning: #fff3cd;
            --warning-border: #ffeba1;
            --danger: #dc3545;
        }

        body {
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
        }

        .container {
            width: 100%;
            max-width: 750px;
            background: var(--card);
            padding: 25px 30px;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }

        .header {
            border-bottom: 2px solid var(--primary);
            padding-bottom: 10px;
            margin-bottom: 20px;
        }

        h1 {
            color: var(--primary);
            font-size: 1.6rem;
            margin: 0 0 5px 0;
        }

        .subtitle {
            color: #6c757d;
            font-size: 0.9rem;
            margin: 0;
        }

        .form-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 15px;
        }

        .form-group {
            display: flex;
            flex-direction: column;
        }

        label {
            font-weight: 600;
            margin-bottom: 6px;
            font-size: 0.88rem;
            color: #333;
        }

        select, input, textarea {
            padding: 10px;
            border: 1px solid #ced4da;
            border-radius: 5px;
            font-size: 0.95rem;
            background-color: #fff;
        }

        select:focus, input:focus, textarea:focus {
            outline: none;
            border-color: var(--secondary);
            box-shadow: 0 0 0 3px rgba(0,86,179,0.15);
        }

        .btn-submit {
            width: 100%;
            background-color: var(--primary);
            color: white;
            border: none;
            padding: 12px;
            font-size: 1rem;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.2s ease;
            margin-top: 10px;
        }

        .btn-submit:hover {
            background-color: var(--secondary);
        }

        /* Tarjeta de Respuesta */
        #result-card {
            display: none;
            margin-top: 25px;
            padding: 20px;
            border-radius: 8px;
            background-color: #f8f9fa;
            border-left: 6px solid var(--primary);
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }

        .badge-platform {
            display: inline-block;
            background-color: #e2e3e5;
            color: #383d41;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .alert-cause {
            background-color: var(--warning);
            border: 1px solid var(--warning-border);
            color: #856404;
            padding: 12px;
            border-radius: 6px;
            margin-bottom: 15px;
            font-size: 0.95rem;
        }

        .solution-box {
            white-space: pre-wrap;
            font-family: inherit;
            background: #ffffff;
            padding: 12px;
            border: 1px solid #e9ecef;
            border-radius: 6px;
            line-height: 1.5;
            font-size: 0.93rem;
        }

        .feedback-container {
            margin-top: 20px;
            padding-top: 15px;
            border-top: 1px solid #dee2e6;
            text-align: center;
        }

        .feedback-btns {
            display: flex;
            gap: 12px;
            margin-top: 10px;
        }

        .btn-fb {
            flex: 1;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            font-size: 0.9rem;
        }

        .btn-yes { background-color: var(--success); color: white; }
        .btn-no { background-color: var(--danger); color: white; }
        .btn-yes:hover { background-color: #218838; }
        .btn-no:hover { background-color: #c82333; }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>⚡ Sistema de Diagnóstico Eléctrico</h1>
        <p class="subtitle">Asistente de Piso de Planta — Prueba Eléctrica y Rework</p>
    </div>

    <form id="diag-form">
        <div class="form-grid">
            <!-- Selección de Plataforma/Vehículo -->
            <div class="form-group">
                <label for="plataforma">Plataforma / Vehículo</label>
                <select id="plataforma" required>
                    <option value="">-- Seleccionar --</option>
                    <option value="KM74">KM74 (Jeep Cherokee)</option>
                    <option value="MP">MP (Jeep Compass)</option>
                </select>
            </div>

            <!-- Selección de Módulo -->
            <div class="form-group">
                <label for="modulo">Módulo Afectado</label>
                <select id="modulo" required>
                    <option value="">-- Seleccionar --</option>
                    <option value="BCM">BCM (Body Control)</option>
                    <option value="IPDM">IPDM (Distribución)</option>
                    <option value="ABS">ABS / Frenos</option>
                    <option value="IPC">IPC (Instrument Panel Cluster)</option>
                </select>
            </div>

            <!-- Entrada de DTC -->
            <div class="form-group">
                <label for="dtc">Código DTC (Opcional)</label>
                <input type="text" id="dtc" placeholder="Ej. U0140, B1025, U0155">
            </div>
        </div>

        <div class="form-group" style="margin-bottom: 15px;">
            <label for="sintoma">Descripción de la falla / Observación del operador</label>
            <textarea id="sintoma" rows="3" placeholder="Describe el síntoma observado en la estación de trabajo..."></textarea>
        </div>

        <button type="submit" class="btn-submit">🔍 Consultar Diagnóstico en Planta</button>
    </form>

    <!-- Tarjeta de Resultados Dinámica -->
    <div id="result-card">
        <span id="badge-plataforma" class="badge-platform"></span>
        <h3 style="margin: 0 0 10px 0; color: var(--primary);">🛠️ Solución Sugerida</h3>
        
        <div id="causa-raiz" class="alert-cause"></div>
        
        <label>Procedimiento de Reparación:</label>
        <div id="pasos-solucion" class="solution-box"></div>
        
        <p style="margin-top: 12px; font-size: 0.9rem;">
            <strong>Pieza / Arnés de referencia:</strong> <span id="pieza-ref"></span>
        </p>
        <p style="font-size: 0.85rem; color: #6c757d;">
            Validaciones exitosas en esta plataforma: <strong id="votos-conteo">0</strong>
        </p>

        <!-- Retroalimentación de Operador -->
        <div class="feedback-container">
            <span style="font-size: 0.9rem; font-weight: 600;">¿Esta solución resolvió la falla en la unidad?</span>
            <div class="feedback-btns">
                <button class="btn-fb btn-yes" onclick="votar(true)">👍 Sí, resuelto en línea</button>
                <button class="btn-fb btn-no" onclick="votar(false)">👎 No, escalar a Calidad</button>
            </div>
        </div>
    </div>
</div>

<script>
    let baseDeDatosFallas = [];
    let fallaActual = null;

    // Cargar base de datos JSON
    fetch('fallas.json')
        .then(response => response.json())
        .then(data => {
            baseDeDatosFallas = data;
            // Cargar votos locales guardados previamente
            baseDeDatosFallas.forEach(item => {
                const votosGuardados = localStorage.getItem('votos_' + item.id);
                if (votosGuardados) item.exito_conteo = parseInt(votosGuardados);
            });
        })
        .catch(err => console.error("Error cargando fallas.json:", err));

    // Lógica de Filtrado Multi-Nivel (Plataforma + Módulo + DTC)
    document.getElementById('diag-form').addEventListener('submit', function(e) {
        e.preventDefault();

        const platSel = document.getElementById('plataforma').value;
        const moduloSel = document.getElementById('modulo').value;
        const dtcIngresado = document.getElementById('dtc').value.trim().toUpperCase();

        // Filtrado por coincidencia exacta
        let resultados = baseDeDatosFallas.filter(falla => {
            const coincidePlataforma = falla.plataforma === platSel;
            const coincideModulo = falla.modulo === moduloSel;
            const coincideDTC = dtcIngresado === "" || falla.dtc.toUpperCase() === dtcIngresado;
            
            return coincidePlataforma && coincideModulo && coincideDTC;
        });

        // Ordenar por efectividad comprobada (mayor conteo de éxitos primero)
        resultados.sort((a, b) => b.exito_conteo - a.exito_conteo);

        const card = document.getElementById('result-card');

        if (resultados.length > 0) {
            fallaActual = resultados[0];
            
            document.getElementById('badge-plataforma').innerText = `Plataforma: ${fallaActual.plataforma} | Módulo: ${fallaActual.modulo}`;
            document.getElementById('causa-raiz').innerHTML = `<strong>Causa Raíz Probable:</strong> ${fallaActual.causa}`;
            document.getElementById('pasos-solucion').innerText = fallaActual.solucion;
            document.getElementById('pieza-ref').innerText = fallaActual.pieza;
            document.getElementById('votos-conteo').innerText = fallaActual.exito_conteo;
            
            card.style.display = 'block';
        } else {
            alert(`No hay registro de esta falla para la plataforma ${platSel} en el módulo ${moduloSel}. Se enviará un reporte a Ingeniería de Calidad.`);
            card.style.display = 'none';
        }
    });

    // Retroalimentación y guardado persistente en navegador
    function votar(exito) {
        if (!fallaActual) return;

        if (exito) {
            fallaActual.exito_conteo++;
            document.getElementById('votos-conteo').innerText = fallaActual.exito_conteo;
            // Guarda el nuevo puntaje en la memoria del dispositivo
            localStorage.setItem('votos_' + fallaActual.id, fallaActual.exito_conteo);
            alert("✅ ¡Validación registrada! La solución ha incrementado su nivel de confianza.");
        } else {
            alert("⚠️ Registro notificado a Ingeniería de Calidad para revisión de arnés o manual de taller.");
        }
    }
</script>

</body>
</html>
